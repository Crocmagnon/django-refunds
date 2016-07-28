# django-refunds
This Django app allows me to add payments I would like to be refunded, my parents can review it and bundle them into a refund.

It then shows the amount they need to refund and they can make the transfer from their online banking account.

## DISCLAIMER
This is not a cost sharing app. Any payment added is supposed to be entirely refund to the payer, or refused.

## Limitations
### User subscription
User subscription is not allowed : the person that deploys the app is responsible for user creation.

### User profiles
Basically three profiles exist :
- Can add/edit/delete payments
- Can add/edit/delete refunds
- Admin

### Target refund
Currently, it's impossible to target a payment to a specific refunder. Payments are visible to all users that can refund.

An improvement could be to be able to target a refund to a specific user, so only him can refund it. This would allow multiple users to share the same database. We could also imagine another system where all refunds from a specific user are by default targeted to the same set of refunders, with the possibility for the payer to change it.
