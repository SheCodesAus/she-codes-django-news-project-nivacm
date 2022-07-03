# Plus Resources: Django Project Starter

Starter code for the Plus Django project.

https://sheltered-hollows-53846.herokuapp.com/news/

Features implemented to create a form for adding new stories.
1) The stories are ordered by date.
2) Form for adding new stories.
3) A new field for an image url was added to the NewsStory model, and this image url is used instead of the default image url images provided in the starter.

Facilitated Feature: Creating a Users app.
I implemented:
1) Functional login/logout buttons.
2) Account view so authors can see their profile information.
3) Create Account functionality, so a new user can sign up to be an author.
4) View stories by a particular author.
5) Show/Hide the relevant information and buttons based on whether the user is logged in/out (e.g.
should only be able to see the button to create a new story if I am logged in).
6) Enable/Disable the relevant features based on whether the user is logged in/out (e.g. should only be
able to create a new story if I am logged in).
7) Add the ability to update and delete stories.