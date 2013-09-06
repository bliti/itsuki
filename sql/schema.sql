/* sqlite3 */

create table if not exists users (
  id integer primary key autoincrement,
  name varchar(255) not null,
  phone varchar(255) not null,
  email varchar(255) not null,
  organization varchar(255) not null,
  status varchar(255) not null,
  role varchar(255) not null
);


create table if not exists receivers (
    id integer primary key autoincrement,
    name varchar(255) not null,
    phone varchar(255) not null,
    receiver_type varchar(255) not null,
    status varchar(255) not null,
    last_call timestamp,
    next_call timestamp,
    user_id integer not null,
    foreign key(user_id) references users(id)
);


create table if not exists calls (
    id integer primary key autoincrement,
    receiver varchar(255) not null,
    dial_datetime timestamp not null,
    result varchar(255) not null,
    user_id integer not null,
    script_id integer not null,
    foreign key(user_id) references users(id),
    foreign key(script_id) references users(id)
); 


create table if not exists scripts (
    id integer primary key autoincrement,
    user_id integer not null,
    script text not null,
    foreign key(user_id) references users(id)
);