import pandas as pd
import duckdb

df = pd.read_csv('https://raw.githubusercontent.com/DanielOX/markov-chain-problem/main/dataset.csv')

df = duckdb.query("""
            SELECT max(a_a) as a_a, max(a_b) as a_b, max(a_c) as a_c,  max(b_a) as b_a, max(b_b) as b_b, max(b_c) as b_c, max(c_a) as c_a, max(c_b) as c_b, max(c_c) as c_c
                    FROM(
                        SELECT 
                            prev_state
                            --dummy key to create groups for every 3 consecutive records
                            ,cast(ceil(row_number() over(order by 1) / 3) as int ) as doc_id 
                            -- transition states origination from a
                            ,CASE WHEN prev_state = 'a' THEN current_state_a ELSE 0 END as a_a
                            ,CASE WHEN prev_state = 'a' THEN current_state_b ELSE 0 END as a_b                    
                            ,CASE WHEN prev_state = 'a' THEN current_state_c ELSE 0 END as a_c
                             
                            -- transition states origination from b
                            ,CASE WHEN prev_state = 'b' THEN current_state_b ELSE 0 END as b_b                    
                            ,CASE WHEN prev_state = 'b' THEN current_state_a ELSE 0 END as b_a
                            ,CASE WHEN prev_state = 'b' THEN current_state_c ELSE 0 END as b_c

                             -- transition states origination from c
                            ,CASE WHEN prev_state = 'c' THEN current_state_c ELSE 0 END as c_c                    
                            ,CASE WHEN prev_state = 'c' THEN current_state_b ELSE 0 END as c_b
                            ,CASE WHEN prev_state = 'c' THEN current_state_a ELSE 0 END as c_a
                        FROM df
                    )
                    GROUP BY doc_id
                    ORDER BY doc_id asc
            """).to_df()
print(df)
