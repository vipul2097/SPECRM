from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')