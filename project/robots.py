"""
Return robot.txt file content.
"""
from django.shortcuts import render_to_response


def robots_file_content(request):
    """
    Return robot.txt file content.
    Add content-type as text plaint.
    And caching time is 24h.
    """
    response = render_to_response('robots.txt')
    time = 24 * 60 * 60
    response['Cache-Control'] = "max-age={0}, public".format(time)
    response['Content-Type'] = 'text/plain'
    return response
