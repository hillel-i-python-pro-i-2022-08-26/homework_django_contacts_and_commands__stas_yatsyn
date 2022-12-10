import logging
from typing import Callable

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from middleware.models import Visit


class SimpleLoggingMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger('django')
        self.logger.info('Init')

    def __call__(self, request: WSGIRequest):

        # Get_user_session__start
        session = request.session
        if not session.session_key:
            session.save()
        session_key = session.session_key
        # Get_user_session__stop

        message = f"Шлях == {request.path}, Користувач == {request.user}, Сесія == {session_key}"

        # Get_response__start
        self.logger.info(f"Перед - {message}")
        response: HttpResponse = self.get_response(request)
        self.logger.info(f"Після - {message}")
        # Get_response__stop

        visit = Visit.objects.filter(session_key=session_key, path=request.path).first()

        if visit is not None:
            count_of_visits = visit.count_of_visits
        else:
            visit = Visit()
            count_of_visits = 0
            if request.user.is_authenticated:
                visit.user = request.user

            visit.path = request.path
            visit.session_key = session_key

        count_of_visits += 1
        session['count'] = count_of_visits
        visit.count_of_visits = session['count']

        visit.save()

        return response
