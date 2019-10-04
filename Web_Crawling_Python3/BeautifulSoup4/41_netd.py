from lib.netd_crawl import getLinks

def main():
    links = []
   
    for num in range(0,10):
        links = links + getLinks(num*10 + 1)
    
    print(len(links))


if __name__ == "__main__":
    main()