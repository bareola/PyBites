def generate_affiliation_link(url):
    return "http://www.amazon.com/dp/" + url[url.find("/dp/")+4:].rsplit("/")[0] + "/?tag=pyb0f-20"
