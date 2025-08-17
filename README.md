# Crowdfunding Back End
Sheila S.

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
- Home page
    - Featured campaigns
    - Most popular campaign (based off amount pledged)
- Create new campaigns
    - Form containing campaign details
    - Ability to submit
    - Nice error pages for validation
- Display campaign
    - Display campaign details
    - Display total amount pledged out of target total
    - Display comments from pledges with names/anonymous
    - Display a default message if there is no pledge
    - Nice error pages for validation
- Pledge
    - Ability to add pledge for logged in user
    - Form containing pledge details (amount, comment, anonymity)
    - Ability to submit
    - Nice error pages for validation for amount and ensuring that pledges are made only for active campaigns
- Logon
    - Form for username and password
    - Error message for validation
- Signup
    - Ability to create new user
    - Error message/page for duplicate usernames or duplidate email
- User page
    - Display username
    - List all pledges made by the user
    - Ability to edit username/email/password is not supported
    - Ability to update pledge (changing pledge amount etc) is not supported 

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL          | HTTP Method | Purpose                              | Request Body | Success Response Code | Authentication/Authorisation |
| ------------ | ----------- | ------------------------------------ | ------------ | --------------------- | ---------------------------- |
| /campaigns   | GET         | List all campaigns                   | N/A          | 200                   | None                         |
| /campaigns   | POST        | Create new campaigns                 | JSON Payload | 201                   | Any logged in user           |
| /campaigns/1 | POST        | Get the details of selected campaign | JSON Payload | 201                   | Any logged in user           |
| /pledges/    | GET         | Fetch all pledges                    | N/A          | 200                   | Any logged in user           |
| /pledges/    | POST        | Create new pledge                    | JSON Payload | 201                   | Any logged in user           |


### DB Schema
![]( ./database.drawio.svg )


### Wouldn't it be cool if...

{{Ideas that seemed cool at the time, but abandoned due to time constraints.}}

- Campaign to have date created, date started and date ended, which would enable campaigns to be scheduled and to have its status automatically updated. But this would need an automated job to be running in the background, continuously checking for dates and updating the campaign status.
- Related to the above, a campaign could have 1 of 4 possible statuses: DRAFT/ACTIVE/COMPLETED/CANCELLED - however this relates to the automatic status update in the point above.
- 