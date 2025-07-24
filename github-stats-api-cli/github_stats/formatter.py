def format_user_stats(data):
    return (
        f"\nGitHub User: {data['login']}\n"
        f"Name: {data.get('name', 'N/A')}\n"
        f"Public Repos: {data['public_repos']}\n"
        f"Followers: {data['followers']}\n"
        f"Following: {data['following']}\n"
        f"Profile: {data['html_url']}\n"
    )