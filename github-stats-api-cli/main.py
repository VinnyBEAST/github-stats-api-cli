from github_stats import fetcher, formatter

def run():
    username = input ("Enter a Github username: ").strip()

    try:
        data = fetcher.get_user_data(username)
        print(formatter.format_user_stats(data))

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    run()

