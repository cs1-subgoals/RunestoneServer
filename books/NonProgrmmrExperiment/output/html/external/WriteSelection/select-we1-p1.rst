WriteSelection-WE1-P1
--------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Write Relational Expressions

   To correctly write selection statements, you must write the conditional expressions correctly. To do this, you generally need to translate the requirements, written in English, to a correct boolean expression. Below are practice questions for this skill.

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: WrSelect-WE1-P1

   .. mchoice:: m-WrSelect-WE1-P1-1
      :answer_a: weight > 100
      :answer_b: weight < 100
      :answer_c: weight >= 100
      :answer_d: weight >> 100
      :correct: a

      Which of the following is the correct Java expression that is equivalent to the English expression "weight is greater than 100"?
      
   
   .. mchoice:: m-WrSelect-WE1-P1-2
      :answer_a: a NOT EQUAL 0
      :answer_b: a NOT= 0
      :answer_c: a != 0
      :answer_d: a !== 0
      :correct: c

      Which of the following is the correct Java expression that is equivalent to the English expression "a not equal to 0"?
      
   
   .. mchoice:: m-WrSelect-WE1-P1-3
      :answer_a: "apple" != "orange"
      :answer_b: apple != orange
      :answer_c: NOT ("apple.equals("orange"))
      :answer_d: apple !== orange
      :correct: b

      Which of the following is the correct Java expression that is equivalent to the English expression "apple and orange are not the same"?
      
   
   .. mchoice:: m-WrSelect-WE1-P1-4
      :answer_a: NOT done
      :answer_b: != done
      :answer_c: !done
      :answer_d: done = false
      :correct: c

      Which of the following is the correct Java expression that is equivalent to the English expression "not done"?


.. activecode:: ac-writeselect-we1-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }