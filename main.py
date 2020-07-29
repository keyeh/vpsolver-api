from flask import escape
from vp_analyzer import HandAnalyzer, DiscardValue

def vpsolver(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'cards' in request_json:
        cards = request_json['cards']
    elif request_args and 'cards' in request_args:
        cards = request_args['cards']
    else:
        cards = 'World'
    return HandAnalyzer(cards).analyze(return_full_analysis=True, return_bestdisc_cnts = True)
