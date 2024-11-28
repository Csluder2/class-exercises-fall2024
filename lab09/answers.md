## SQL Questions
1. SELECT - Retrieving Data. Write a query to list the titles and release years of all movies in the film table.

SELECT release_year, year FROM film; 


2. WHERE - Filtering Data. Write a query to find all customers whose last name starts with the letter 'S'.

SELECT last_name FROM customer where last_name LIKE 'S%';


3. ORDER BY - Sorting Results. List all films titles and their durations, sorted by their rental duration in descending order. If two films have the same rental duration, sort them alphabetically by title.

SELECT title, rental_duration, length FROM film ORDER BY rental_duration DESC, title ASC;


4. JOIN - Combining Tables. Write a query to list all films along with their categories. Show the film title and category name.

SELECT title AS film_title, name AS category_name
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id;



5. AGGREGATE FUNCTIONS - Summarizing Data. Write a query to find the average rental duration for movies in each category.

SELECT category.name AS category_name, AVG(film.rental_duration) AS avg_rental_duration
FROM film 
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
GROUP BY category.name;


6. COUNT - Counting Rows. Write a query to count how many films are in the Action category.

SELECT COUNT(film.film_id) AS action_film_num
FROM film 
INNER JOIN film_category on film.film_id = film_category.film_id 
INNER JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Action';


7. INSERT - Adding Data. Insert a new customer into the customer table. The new customer should have a first name, last name, email, and be linked to an existing store.

INSERT INTO customer (first_name, last_name, email, store_id, address_id)
VALUES ('John', 'Snow', 'JohnSnow12@example.com', 1, 10);


8. UPDATE - Modifying Data. Update the rental rate of all films in the Comedy category, increasing it by 10%.

UPDATE film
SET rental_rate = rental_rate * 1.10 
WHERE film_id IN 
(SELECT film.film_id
 FROM film 
 INNER JOIN film_category ON film.fim_id = film_category.film_id
 INNER JOIN category ON film_category.category_id = category.category_id
 WHERE category.name = 'Comedy'
 );


9. DELETE - Removing Data. Write a query to delete all films that have never been rented. Make sure to use a subquery to identify the films that haven't been rented.

DELETE FROM film
WHERE film_id NOT IN (
    SELECT DISTINCT inventory.film_id
    FROM rental
    INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
);

10. CREATE TABLE & ALTER TABLE - Managing Database Structure. Create a new table called movie_reviews with columns for review_id, film_id, reviewer_name, rating, and comments. Then, add a foreign key constraint linking film_id to the film table.

CREATE TABLE movie_reviews (
    review_id SERIAL PRIMARY KEY,
    film_id INT,
    reviewer_name VARCHAR(100),
    rating INT,
    comments TEXT,
    FOREIGN KEY (film_id) REFERENCES film(film_id)
);



## SQLAlchemy Questions

1. Understanding SQLAlchemy Automap: How do you think the `AutoModels` class works to dynamically generate SQLAlchemy ORM models from the database schema?

Uses SQLAlchemy's automap function to do so (by reducing the need to define each model class). 

2. Async Database Operations: Explain the use of asynchronous database sessions in this script. Why does the script use AsyncSession instead of a regular Session, and how does this improve the efficiency of database operations?
It uses it because it is more effecient than the standard one, as it can handle multiple databases and their requests easier. 


3. SQLAlchemy Query Construction: In the `model_examples` function, there is a query that selects all customers whose last names start with the letter "P". See if you can write another questy that selects customers whose first name ends with the letters "n" or "a" using SQLAlchemy syntax.

async with AsyncSession(engine) as session:
    customers = await session.execute(
        select(Customer).where(
            Customer.first_name.endswith("n") | Customer.first_name.endswith("a")
        )
    )
    for customer in customers.scalars().all():
        print(customer.first_name)


4. In the `raw_sql_examples` function, there are two ways to execute SQL queries: directly via the engine using conn.execute() and using an ORM session with session.execute(). Discuss the pros and cons of executing raw SQL directly compared to using SQLAlchemy’s ORM methods.
Hint: Consider the trade-offs in terms of readability, safety (e.g., SQL injection risks), and flexibility when using raw SQL versus ORM abstractions.

RAw SQL PROS:
- More flexible
- Better performance

CONS
- Harder to read
- SQL injection attacks (we talked a good bit about this in databases)
- LACK of benefits from ORM methods


SQL Alchemy ORM PROS:
- Easier to read
- Better security 

CONS:
- Worse performance
- Less flexible