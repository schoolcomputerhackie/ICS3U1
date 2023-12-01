Step one: Open up https://reqbin.com/ and put this under headers:
Authorization: Token <token> 
(replace the <token> with your token.)
Step two: Open up any activity you want to be completed, and press submit (it doesn't have to be done)
Step three: Open up inspect element and check under the network tab for a post request titled "Points"
Step four: Click on that post request and under payload, click "view source".
Step five: Copy whats in there, it should look something like this if you've done it right.
{"submission_id":22876858,"points":0,"score":"FAIL","file_version":[82534201,8]}
Step six: Paste this under the "Content" area in the reqbin you have open.
Step seven: Set the area where it says "FAIL" to "PASS" and set the points to the amount of points you want to get.
Voila! You now have an infinite point glitch. Set the number right beside the "points" area from a 0 to whatever number of points you want to get and you're done.
