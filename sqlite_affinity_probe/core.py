import sqlite3,math
from .common import number

def scalar(x):
 if x is not None and (isinstance(x,bool)or not isinstance(x,(int,float,str))):raise ValueError('scalar')
 if isinstance(x,(int,float)):number(x,-1e15,1e15)
 if isinstance(x,str)and len(x)>10000:raise ValueError('text')
 return x
def run(data):
 values=data['values'];affinities=data.get('affinities',['TEXT','NUMERIC','BLOB']);predicate=data['predicate'];op=predicate['operator']
 if op not in ('=','!=','<','<=','>','>=','IS','IS NOT')or not 1<=len(affinities)<=5 or len(set(affinities))!=len(affinities)or len(values)>1000:raise ValueError('bounds')
 values=[scalar(x)for x in values];param=scalar(predicate['value']);results=[]
 for affinity in affinities:
  if affinity not in ('TEXT','INTEGER','NUMERIC','REAL','BLOB'):raise ValueError('affinity')
  c=sqlite3.connect(':memory:')
  try:
   c.execute('CREATE TABLE items(v '+affinity+')');c.executemany('INSERT INTO items VALUES (?)',[(v,)for v in values]);stored=[{'row':r[0],'value':r[1],'storage_class':r[2]}for r in c.execute('SELECT rowid,v,typeof(v) FROM items ORDER BY rowid')];matched=[r[0]for r in c.execute('SELECT rowid FROM items WHERE v '+op+' ? ORDER BY rowid',(param,))];results.append({'affinity':affinity,'stored':stored,'matching_rows':matched})
  finally:c.close()
 return {'variants':results,'same_matching_rows':len({tuple(r['matching_rows'])for r in results})<=1,'sqlite_version':sqlite3.sqlite_version,'model':'native_sqlite_scalar_affinity_probe'}
