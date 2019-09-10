import json

from requests_oauthlib import OAuth2Session

from _const import CLIENT_ID,CLIENT_SECRET,REDIRECT_URI

def auth():

    scope=['public','private','stats']
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI,scope=scope)
    authorization_url, state = oauth.authorization_url('https://api.vimeo.com/oauth/authorize')

    resp = _redirect(authorization_url)
    token = oauth.fetch_token('https://api.vimeo.com/oauth/access_token',
                              authorization_response=resp,
                              client_secret=CLIENT_SECRET)
    return oauth

def make_request(oauth):

    start_date = '2019-09-09'
    end_date = '2019-09-09'

    rURL = 'https://api.vimeo.com/me/videos/stats?group_by=embed_path&start_date=2018-09-10&end_date=2019-09-10&per_page=50&filter_embed_domains=filmfreeway.com&sort=plays&direction=desc&fields=url%2Cplays%2Cfinishes%2Cloads%2Cdownloads%2Cwatched&csv=https%3A%2F%2Fapi.vimeo.com%2Fme%2Fvideos%2Fstats%3Fstart_date%3D2018-09-10%26end_date%3D2019-09-10%26fields%3Durl.domain%2Cplays%2Cfinishes%2Cloads%2Cdownloads%2Cwatched.mean_percent%26group_by%3Dembed_domain%26per_page%3D15000%26sort%3Dplays&page=1'
    r = oauth.get(rURL)
    return r.json()
