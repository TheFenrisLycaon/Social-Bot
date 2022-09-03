from urllib.request import parse_http_list
import requests, urllib.request
import os, sys, time

counter = 0


def getPosts(subreddit, postLimit):
    url = "http://www.reddit.com/r/" + subreddit + "/.json?limit=" + str(postLimit)
    headers = {"User-Agent": "Reddit Wallpaper Scraper 1.0"}
    r = requests.get(url, headers=headers)
    # print(r.status_code)
    if r.status_code == requests.codes.ok:
        data = r.json()
        print("Sleeping for 5 seconds...\n")
        time.sleep(5)
        return data["data"]["children"]
    else:
        print("Sorry, but there was an error retrieving the subreddit's data!")
        return None


def saveImages(posts, scoreLimit, save_dir="reddit_wallpapers"):
    for post in posts:
        url = post["data"]["url"]
        score = post["data"]["score"]
        # title = post['data']['title']
        if "i.imgur.com" in url and score > scoreLimit:
            try:
                saveImage(url, save_dir)
            except:
                pass
        if "i.redd.it" and "com" not in url and score > scoreLimit:
            try:
                saveImage(url, save_dir)
            except:
                pass


def saveImage(url, save_dir):
    global counter
    save_dir = makeSaveDir(save_dir)
    dot_location = url.rfind(".")
    filename = (
        save_dir + "img-{}".format(counter) + url[dot_location : dot_location + 4]
    )
    print("Saving " + str(filename) + "!\n")
    counter += 1
    urllib.request.urlretrieve(url, filename)


def makeSaveDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir + "/"


def downloadImagesFromReddit(
    subreddits, postLimit=int(input("Enter Number of images::\t")), scoreLimit=1
):
    for subreddit in subreddits:
        posts = getPosts(subreddit, postLimit)
        saveImages(posts, scoreLimit, subreddit.lower())
    print(str(counter) + " images have been scraped!")


def main():
    if len(sys.argv) > 1:
        downloadImagesFromReddit(sys.argv[1:])
    else:
        downloadImagesFromReddit(["memes"])


if __name__ == "__main__":
    main()
