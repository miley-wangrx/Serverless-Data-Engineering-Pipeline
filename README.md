
# Part of Speech Tagging using AWS Lambda

<img width="600" alt="image" src="https://user-images.githubusercontent.com/88390268/164373808-2ca34668-6a95-48a1-a247-47c111dce96f.png">
Part of speech (POS) tagging is the process of marking up a word in a text corresponding to a part of speech. In this project, I build an AWS Lambda function on AWS Cloud9. 

## Build and Deploy

1.  `sam init`
2.  `sam build`
3.  `sam deploy --guided`

## Deploy and Testing

Tested in two ways:  

`sam local invoke`
`sam local start-api`

Then curl `curl http://127.0.0.1:3000/hello`

* API Gateway
* CloudWatch Logs
* IAM Security settings

## Outcomes
* Deployed Stack
  <img width="1577" alt="image" src="https://user-images.githubusercontent.com/88390268/164374939-3bd83bf0-acff-496e-9306-2fb1ed04f6e8.png">

  <img width="900" alt="image" src="https://user-images.githubusercontent.com/88390268/164375029-28e3c211-f19a-4b7f-b972-4f64307c5808.png">
* Testing with sentence `Hey, are you there?`
  <img width="900" alt="image" src="https://user-images.githubusercontent.com/88390268/164375107-ef721e33-5d1c-4211-956b-0a1dff7ba7e0.png">


