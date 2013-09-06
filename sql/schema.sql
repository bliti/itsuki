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
    user_id varchar(255) not null,
    name varchar(255) not null,
    phone varchar(255) not null,
    receiver_type varchar(255) not null,
    status varchar(255) not null,
	last_call timestamp,
	next_call timestamp,
    foreign key(user_id) references users(id)
	
); 