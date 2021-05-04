SET NAMES UTF8;
CREATE TABLE user_info (
	user_id INT NOT NULL AUTO_INCREMENT,
	user_email VARCHAR(100) NOT NULL,
	blog_id CHAR(4),
	PRIMARY KEY(user_id)
);
