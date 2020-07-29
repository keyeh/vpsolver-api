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
        return 400
    
    analysis = HandAnalyzer(cards).analyze(return_full_analysis=False, return_bestdisc_cnts = False)
    return {"hand": analysis[0], "expected_value":analysis[1]}


def convertHandStringFormat(handStr):
    n = 2
    a = [handStr[i:i+n][::-1] for i in range(0, len(handStr), n)]
    return ''.join(a).upper()
