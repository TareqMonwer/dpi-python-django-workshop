#### Record Fields/Attributes
+ plan_name,
+ time_starts,
+ time_ends,
+ label, (top priority, mid priority, low priority)
+ track_resources,
+ track_author,
+ created_at,
+ updated_at,
+ is_active,


#### Expected action with these fields:

+ Get all plans
+ Get plans by priority group
+ Get plans by track_author
+ Read track details 
#### ADVANCE:
+ is_active should be false if time_ends is past
+ label should change based on days remaining for time_ends