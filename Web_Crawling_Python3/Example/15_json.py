# 밑에 두줄은 동일
[{"name":"dongjin", "age":"32"}]
[1]

json_obj = {"name":"dongjin"}
print(json_obj)

json_obj = {"name":"dongjin", "age":"25"}
print(json_obj)

json_obj = {"name":"dongjin",
            "age":"25",
            "where":"등촌동",
            "phone_number":"010-1234-5678"
            }
print(json_obj)

json_obj = {"name":"dongjin",
            "age":"25",
            "where":"등촌동",
            "phone_number":"010-1234-5678",
            "friends":[{"name":"yoo", "age":"20"}]
            }
print(json_obj['friends'])

json_obj = {"name":"dongjin",
            "age":"25",
            "where":"등촌동",
            "phone_number":"010-1234-5678",
            "friends":[
                {"name":"yoo", "age":"20"},
                {"name":"huynjin", "age":"22"}
            ]
            }
friends = json_obj['friends']
for friend in friends:
    print(friend['name'])