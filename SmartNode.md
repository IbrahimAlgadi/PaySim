# PaySim For Smart Node Payment System

**Description**:  So when you try to work with Smart Node there is a specific 
steps you have to go through, as specified by Smart Node Specifications Document 
version 1.0.0

 
1 - You go to smart node and sign with them a contract, they will give you api access
very fast and in a very short time, you get your user and token that you will be using
during your test and your production.

2 - Then you are going to call the payment end point and send in the POST params
the following 
* using the PaySim test sand box you will have 2 card numbers giving you 2 responses
(the first one is 2222222222222222) this will give you always success, and the other
is (4444444444444444) this will give you failed payment, then any other card will
always return Error.

and sending your payload with it
```
POST Request to /payment
{
  "card": "2222222222222222",
  "amount": 400,
  "expDate": "12/21",
  "pin": 1212,
  "user": "your smart node user",
  "token": "your smart node token"
}

curl -X POST "http://localhost:5000/payment" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"card\":\"2222222222222222\",\"amount\":400,\"expDate\":\"12/21\",\"pin\":1212,\"user\":\"your smart node user\",\"token\":\"your smart node token\"}"

```
In the PaySim the request will be like
![](./assets/Smart%20Node%201.PNG)

3 - Then there will be a response from Smart Node in case of success it will give you

```

{
  "status": true
}

```
In the Smart Node the response will be like
![](./assets/Smart%20Node%202.PNG)

4 - The response is case of failure it will give you

```

{
  "status": false,
  "msg": "EBS Standard Error Messages"
}

```

### Easy Right

- You take this response and send it back to the client informing him about the
action happened and use the status to give the client access to the service
he is requesting.