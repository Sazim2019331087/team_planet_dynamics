CREATE DATABASE planet_dynamics;

USE planet_dynamics;

CREATE TABLE learner(
    email varchar(100),
    name varchar(100),
    code varchar(100)
);

CREATE TABLE coins(
    email varchar(100),
    coin varchar(100)
);

CREATE TABLE user_image(
    email varchar(100),
    image_path varchar(100)
);

CREATE TABLE friends(
    from_ varchar(100),
    to_ varchar(100)
);

CREATE TABLE blogs(
    blog_id varchar(100),
    email varchar(100),
    blog_title varchar(300),
    blog_content varchar(2000),
    blog_subject varchar(500),
    rating varchar(200),
    blog_time varchar(100)
);

