import unittest
from sqlite_affinity_probe import run
class Tests(unittest.TestCase):
 def test_native_affinity_changes_business_match(self):
  r=run({'values':['01','1','1x',None,1],'affinities':['TEXT','NUMERIC','BLOB'],'predicate':{'operator':'=','value':1}});self.assertEqual([x['matching_rows']for x in r['variants']],[[2,5],[1,2,5],[5]]);self.assertFalse(r['same_matching_rows'])
 def test_storage_classes_are_observed_not_guessed(self):
  r=run({'values':['01','1x',None],'affinities':['NUMERIC'],'predicate':{'operator':'IS','value':None}});self.assertEqual([x['storage_class']for x in r['variants'][0]['stored']],['integer','text','null']);self.assertEqual(r['variants'][0]['matching_rows'],[3])
 def test_parameter_text_is_bound_not_executed(self):
  r=run({'values':["x' OR1=1--",'other'],'predicate':{'operator':'=','value':"x' OR1=1--"}});self.assertTrue(all(x['matching_rows']==[1]for x in r['variants']))
 def test_operator_and_type_injection_rejected(self):
  for change in [{'affinities':['TEXT); DROP TABLE items;--']},{'predicate':{'operator':'=1;','value':1}}]:
   with self.assertRaises(ValueError):run({'values':[1],'predicate':{'operator':'=','value':1},**change})
