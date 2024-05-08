CREATE TYPE loyalty AS ENUM ('none', 'beginner', 'regular', 'vip');

ALTER TABLE passengers
ADD COLUMN IF NOT EXISTS loyalty_program loyalty;