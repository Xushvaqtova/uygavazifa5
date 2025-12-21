# 5-misol
# Eng ko`p zakaz qilingan mahsulot turi bo`yicha hisobot shakllantiring

# select c.category_name, count(*) from order_details od
# inner join products p on (od.product_id = p.product_id)
# inner join categories c  on (p.category_id = c.category_id)
# group by c.category_name order by total_orders DESC limit 1;
#
#
# -- 6-misol
# -- Amerikada yashovchi eng faol hodimlar haqida ma`lumot shakllantiring
#
# -- select e.employee_id,e.country,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country='USA'
# -- group by e.employee_id,e.first_name,e.last_name,e.country
# -- having count(o.order_id)=(select count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country='USA'
# -- group by e.employee_id,e.first_name,e.last_name,e.country
# -- order by count(o.order_id) desc limit 1)
# -- order by count(o.order_id) desc
#
# -- 7-misol
# -- Qaysi davlatdagi hodimlar eng faol ishlashi haqidagi hisobot shakllantiring
#
# -- select e.country, count(order_id) from employees as e
# -- inner join orders o on o.employee_id=e.employee_id
# -- group by e.country
# -- having count (o.order_id)=(select count(o.order_id) from employees as e
# -- inner join orders o on o.employee_id=e.emloyee_id
# -- group by e.country order by e.count desc limit 1)


# 9-misol
# Eng kam buyurtma qilingan mahsulotlar

# select p.product_name, sum(od.quantity) as total_qty from products p
# inner join order_details od on p.product_id = od.product_id
# group by p.product_name order by total_qty LIMIT 1;












