I did not get Render to work for my project. 

Originally, the app did work, but now after reverting back to a previous commit neither the app or the editor server on DevEdu work properly.

For AI usage, I used ClaudeAI to help out with the templates along with routing them to the URLs.

To run the tests, which document the CRUD principles of the models, use "python manage.py test" in the same directory as manage.py.

The models are as follows:

The Movie model, which has a title, description, release date, and duration. 
The Seat model, which has a seat number and booking status.
The Booking model, which has a ForeignKey movie and seat, along with a username and booking date. 