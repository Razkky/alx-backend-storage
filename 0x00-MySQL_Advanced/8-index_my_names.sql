-- Create an Index on table names and column name

CREATE INDEX idx_name_first ON names (LEFT(name, 1));
