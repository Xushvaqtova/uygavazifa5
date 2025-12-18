# -- create table if not exists categories(
# -- category_id smallint not null,
# -- category_name character varying(25) not null,
# -- description text,
# -- picture bytea
# -- );
#
#
# -- create table if not exists products(
# -- product_id smallint not null,
# -- product_name character varying(40) not null,
# -- supplier_id smallint,
# -- category_id smallint,
# -- quantity_per_unit character varying(25),
# -- unit_price real,
# -- units_in_stock smallint,
# -- units_on_order smallint,
# -- reorder_level smallint,
# -- discontinued integer not nu
# -- )
#
#
# -- create table if not exists suppliers(
# -- supplier_id smallint not null,
# -- company_name character varying(40) not null,
# -- contact_name character varying(35),
# -- contact_title character varying(30),
# -- address character varying(60),
# -- city character varying(15),
# -- region character varying(15),
# -- postal_code character varying(10),
# -- country character varying(15),
# -- phone character varying(24),
# -- fax character varying(24),
# -- homepage text
# -- );
#
#
# -- create table if not exists order_details(
# -- order_id smallint not null,
# -- product_id smallint not null,
# -- unit_price real not null,
# -- quantity smallint not null,
# -- discount real not null
# -- );
#
#
# -- create table if not exists orders(
# -- order_id smallint not null,
# -- order_date date,
# -- required_date date,
# -- shipped_date date,
# -- ship_via smallint,
# -- freight real,
# -- ship_name character varying(50),
# -- ship_address character varying(60),
# -- ship_city character varying(15),
# -- ship_region character varying(20),
# -- ship_postel_code character varying(15),
# -- ship_country character varying(51)
# -- );
#
#
# -- alter table categories
# -- add constraint pk_categories
# -- primary key (category_id);
#
#
# -- alter table suppliers
# -- add constraint pk_suppliers
# -- primary key (supplier_id);
#
#
# -- alter table products
# -- add constraint pk_products
# -- primary key (product_id);
#
#
# -- alter table orders
# -- add constraint pk_orders
# -- primary key (order_id);
#
# -- alter table order_details
# -- add constraint pk_order_details
# -- primary key (order_id, product_id);
#
#
# -- alter table products
# -- add constraint fk_products_categories
# -- foreign  key (category_id)
# -- references categories (category_id);
#
#
# -- alter table products
# -- add constraint fk_products_suppliers
# -- foreign key (supplier_id)
# -- references suppliers(supplier_id);
#
#
# -- alter table order_details
# -- add constraint fk_order_details_orders
# -- foreign key (order_id)
# -- references orders(order_id)
# -- on delete cascade;
#
#
# -- alter table order_details
# -- add constraint fk_order_details_products
# -- foreign key (product_id)
# -- references products(product_id);
#
#
# -- insert into categories(category_id,category_name,description) values
# -- (1,'name1', 'drinks'),
# -- (2,'name2', 'sauses'),
# -- (3,'name3', 'sweets'),
# -- (4,'name4', 'milk products'),
# -- (5,'name5', 'fish');
#
# -- insert into suppliers (supplier_id,company_name,country) values
# -- (1,'suppl A', 'USA'),
# -- (2,'suppl B', 'Germany'),
# -- (3,'suppl C', 'France'),
# -- (4,'suppl D', 'Japan'),
# -- (5,'suppl E', 'China');
#
# -- insert into products(product_id, product_name,supplier_id,category_id,unit_price,units_in_stock,discontinued) values
# -- (1,'tea',1,1,10.5,50,0),
# -- (2,'coffee',2,1,15.0,40,0),
# -- (3,'cheese',3,4,25.0,20,0),
# -- (4,'chocolate',4,3,8.0,100,0),
# -- (5,'fish',5,5,30.0,15,0);
#
#
# -- insert into orders(order_id,order_date,ship_country) values
# -- (1,'2024-01-01','USA'),
# -- (2,'2024-01-02','Germany'),
# -- (3,'2024-01-03','France'),
# -- (4,'2024-01-04','Japan'),
# -- (5,'2024-01-05','China');
#
#
# -- select category_id, product_name from products where category_id > 3;
#
# -- select * from customers where country = 'Brazil' AND company_name like '__n%';
#
# -- select * from customers where country in 'UK' AND company_name like '%a__';
#
# -- select AVG(unit_price) FROM products;
#
# -- select * from orders where to_char(order_date, 'YYYY-MM')='1997-07'
#
# -- select * from products where category_id = 1 order by unit_price desc limit 1;