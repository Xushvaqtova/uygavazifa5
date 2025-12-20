select c.category_name, count(*) from order_details od
inner join products p on (od.product_id = p.product_id)
inner join categories c  on (p.category_id = c.category_id)
group by c.category_name order by total_orders DESC limit 1;