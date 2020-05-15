# Flack
This app was created as Project 2 for CS50 Web Programming.

It's a Slack-like messaging app, built using Flask and Javascript. This application doesn't use a database, so if the server is stopped, all the data is lost. The project's main goal was the get more comfortable with AJAX and web sockets. It runs on localhost. The website has not been styled and therefor looks terrible, but this wan't the goal of this project.

When a user first loads the site in, he's asked to give a username. This username is stored in localStorage, and cannot be changed. It's locked to that particular browser. The user can then create channels, and send meesages in each one. Since the app runs on localhost, the only way to have another user, is to open another browser on the same system. That user is also asked to give a username, then he can join existing channels and chat with "other" users, or create new channels. New channels and messages appear for every user automatically, without reloading. 
