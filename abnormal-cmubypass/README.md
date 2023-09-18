# Abnormal CMU Bypass Pack
### Uploading Code to CMU Project using HTTP
- Using my [Custom Formatter](https://linksoon), format your Python file and copy the output string
- Use an HTTP test site like [REQBIN](https://reqbin.com/) and fill in the following values:<br>
---
Content:

```
{
  "path": "PROJECT NAME",
  "fileOwner": "USERNAME",
  "content": "OUTPUT PYTHON STRING HERE",
  "contentType": "text/python",
  "csvStatus": null,
  "overwrite": true
}
```

Headers: (MAKE SURE TO USE HEADERS NOT AUTHORIZATION)

```
Authorization: Token <TOKEN PART HERE>
```

