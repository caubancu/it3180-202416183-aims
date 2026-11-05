# AIMS-mini use cases

```mermaid
flowchart TD
    Customer[Customer] --> Browse[Browse DVD catalogue]
    Customer --> Search[Search DVD by title]
    Customer --> Cart[Manage shopping cart]
    Cart --> Add[Add DVD]
    Cart --> Total[Calculate total cost]
    Cart --> Print[Print cart]
```

## Main flow
1. The customer browses or searches the DVD catalogue.
2. The customer adds selected DVDs to the cart, subject to the 20-item limit.
3. The application displays the cart and calculates its total cost.
