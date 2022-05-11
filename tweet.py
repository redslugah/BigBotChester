import database
import tweepy as tp
import time

def readConfig():
    f = open("config.cfg", "r")
    data = f.read().splitlines()
    return data

def tweet(content):
    data = readConfig()
    #db info
    host = data[0]
    user = data[1]
    passw = data[2]
    db = data[3]
    #credenciais
    api_key = data[4]
    api_secret = data[5]
    access_token = data[6]
    access_secret = data[7]
    posted = 'No'
    
    #login na api twitter
    auth = tp.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)
    
    #finalizar a formação do jeito que quero que seja tweetado e realizar o tweet
    firstOne = content.title.split(' - ', 1)
    author = firstOne[0]
    title = firstOne[1]
    if len(title) > 100:
        title = title[:100] + '...'
    try:
        api.update_status(author + ' on: ' + title + ' #pathofexile\n' + content.link)
    except Exception as e:
        print('An exception occured, not posted. Error: %s', e)
    else:
        posted = 'Yes'
        post(author, title, content.link, posted, host, user, passw, db)
        print('Posted: \n' + author + ' on: ' + title + ' #pathofexile\n' + content.link)

def post(author, title, link, posted, host, user, passw, db):
    connection = database.createDbConnection(host, user, passw, db)
    colon = "'"
    if any(c in colon for c in title):
        title = title[:title.find("'")] + '\\'+ title[title.find("'"):]
    query = "INSERT INTO BBCPOSTS (BBCLKPST, BBCNMSTF, BBCPOSTD, BBCPOSTT) VALUES ('"+link+"', '"+author+"', '"+posted+"', '"+title+"');"
    database.executeQuery(connection, query)
