class Response:
    list_all_users = "li:has-text(\"List users\")"

    @staticmethod
    def get_list_of_all_users_firstname(page):
        page.goto("https://reqres.in/")
        with page.expect_response("https://reqres.in/api/users?page=2") as response_info:
            page.click(Response.list_all_users)

        response = response_info.value

        print(response.ok)
        print(response.status)
        print(response.request)
        print(response.body)

        response_json = response.json()
        print(response_json)

        lst_names = []
        for user in response_json['data']:
            lst_names.append(user["first_name"])

        return lst_names



