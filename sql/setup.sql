CREATE USER calendar_this WITH PASSWORD 'password' superuser;

CREATE DATABASE calendar_this_dev WITH OWNER calendar_this;

CREATE TABLE appointments (
  id serial PRIMARY KEY,
  name varchar(200) NOT NULL,
  start_datetime timestamp NOT NULL,
  end_datetime timestamp NOT NULL,
  description text NOT NULL,
  private boolean NOT NULL
);

INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
  VALUES ('Tag appointment', '2020-10-13  14:00:00', '2020-10-13 15:00:00', 'An appointment for Tag', FALSE);
