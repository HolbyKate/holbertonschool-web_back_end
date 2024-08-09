-- Create a trigger that decreases quantity of an item after adding new order
CREATE Trigger order_decrease BEFORE INSERT on orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
