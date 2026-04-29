# Data Analyzer (JSONPlaceholder API)

## Overview

The Data Analyzer is a Python-based application that interacts with the JSONPlaceholder API to fetch and analyze user, post, and comment data. It processes the retrieved data and provides meaningful insights such as user activity, post engagement, and comment distribution.

## Features

* Fetches data from JSONPlaceholder API:

  * Users
  * Posts
  * Comments
* Maps relationships:

  * Users → Posts
  * Posts → Comments
* Provides analytical insights:

  * Number of posts per user
  * Number of comments per post
  * Most active user (based on post count)
  * Post with highest number of comments
  * Average number of comments per user
* Interactive menu-driven interface for easy navigation

## Functional Insights

### 🔹 User → Posts Mapping

Displays each user along with the list and count of posts created.

### 🔹 Post → Comments Mapping

Shows each post with associated comment IDs and total comment count.

### 🔹 Most Active User

Identifies the user who has created the highest number of posts.

### 🔹 Post with Highest Comments

Finds the post that has received the maximum number of comments.

### 🔹 Average Comments per User

Calculates the average number of comments received across all posts for each user.

## Example Output

```id="d1k3lm"
Fetching data
Data Loaded Successfully

--------Menu--------
1. Show User → Post count
2. Show Post → Comment count
3. Most Active User
4. Post with Highest Comments
5. Average Comments per User
6. Exit
```

```id="k92plx"
User 1 -> Posts : [1, 2, 3, 4] (Total : 4 posts)
User 2 -> Posts : [5, 6, 7] (Total : 3 posts)
```

```id="z7q1sn"
Post 1 -> Comments : [1, 2, 3] (Total : 3 comments)
```

```id="m8x4pd"
Most Active user :  Leanne Graham
Number of posts:  10
```

```id="w5r2ka"
Post with Highest comments
Post id :  1
Title :  sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Total comments :  5
```

```id="y9v3te"
Leanne Graham -> 5.0
Ervin Howell -> 3.6
```
## Working Principle

The system follows a structured approach:

* Fetches data from the API using HTTP requests
* Organizes data using dictionary mappings for efficient lookup
* Performs computations on mapped data to generate insights
* Provides results through a menu-driven interface for user interaction

## Summary

This project demonstrates API integration, data mapping, and analytical processing using Python. It highlights the ability to transform raw API data into meaningful insights through structured logic and efficient data handling.
