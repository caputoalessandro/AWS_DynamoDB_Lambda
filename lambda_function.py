def lambda_handler(event: any, context: any):
    user = event["user"]
    visit_count = 0
    message = f"Hello {user}! You have visited this page {visit_count} times!   "
    return {"message": message}


if __name__ == "__main__":
    event = {"user": "Ale_local"}
    print(lambda_handler(event, None))