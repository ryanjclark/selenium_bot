# selenium_bot   
  
This selenium script checks out one of my websites (eateryexchange.com), fills the first form, and tests the banner result.  
  
  
Using Selenium Grid, two more workflows will be checked in this project:  
  
Workflow A: 
1. User hits seller-registration
2. User fills out this form, becomes a user, and is routed to seller-registration-2
3. User fills out this part of the form and is routed to seller-registration-3
4. User fills out this part of the form and is routed to checkout
5. User fills out checkout and is routed to seller-finish
6. User requests educational material  
  
Workflow B (purposefully broken):
1. User hits buyer-registration
2. User fills out form, becomes a user, and is routed to buyer-finish
3. User clicks on the button to be taken to the map of restaurants for sale
