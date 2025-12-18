# -- select to_char(orders.order_date, 'MM'), count(DISTINCT orders.order_id) from orders
# -- inner join order_details od on (orders.order_id = od.order_id)
# -- inner join products p on (od.product_id = p.product_id)
# -- where p.category_id = 1 and od.unit_price > 10 and to_char(orders.order_date, 'YYYY')='1996'
# -- group by to_char(orders.order_date, 'MM');
#
#
# -- select s.supplier_id, s.company_name, s.contact_name from suppliers s
# -- inner join products p on (s.supplier_id = p.supplier_id)
# -- inner join order_details od on (p.product_id = od.product_id)
# -- inner join orders o on (od.order_id = o.order_id)
# -- where p.category_id = 3 and to_char(o.order_date, 'YYYY-MM')='1997-07'
# -- and p.product_id= (select product_id from products where category_id = 3
# -- order by unit_price ASC limit 1);
#
#
# -- select distinct s.supplier_id, s.company_name from orders o
# -- inner join order_details od on (o.order_id = od.order_id)
# -- inner join products p on (od.product_id = p.product_id)
# -- inner join suppliers s on (p.supplier_id = s.supplier_id)
# -- and to_char(o.order_date, 'YYYY-MM') = '1998-03'
#
#
# -- select c.category_name, p.product_name, SUM(od.quantity) from categories c
# -- inner join products p on (c.category_id = p.category_id)
# -- inner join order_details od on (p.product_id = od.product_id)
# -- inner join orders o on (od.order_id = o.order_id)
# -- where to_char(o.order_date, 'YYYY') = '1996' and p.unit_price = (
# -- select max(p2.unit_price) from products p2 where p2.category_id = c.category_id)
# -- group by c.category_name, p.product_name;
#
#
# -- select s.company_name, s.supplier_id, s.contact_name, s.country from customers c
# -- inner join orders o on (c.customer_id = o.customer_id)
# -- inner join order_details od on (o.order_id = od.order_id)
# -- inner join products p on (od.product_id = p.product_id)
# -- inner join suppliers s on (p.supplier_id = s.supplier_id)
# -- where c.country = 'USA' and s.country = 'USA' and to_char(o.order_date, 'YYYY') = '1997';
#
#
# -- select s.supplier_id, s.company_name, s.contact_name, s.country from suppliers s
# -- inner join products p on (s.supplier_id = p.supplier_id)
# -- inner join order_details od on (p.product_id = od.product_id)
# -- inner join orders o on (od.order_id = o.order_id)
# -- where p.category_id = 5 and to_char(o.order_date, 'YYYY')='1997';
#
#
#
# -- select ship_city, to_char(order_date, 'MM'), count(order_id) from orders
# -- where ship_city = 'USA' and to_char(order_date, 'YYYY')='1997'
# -- group by ship_city, to_char(order_date, 'MM')
# -- order by ship_city;
