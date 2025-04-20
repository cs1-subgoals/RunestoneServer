WrClasses-WE1-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Writing a Class 1/4

   1. Name it 


   2. Differentiate class-level (static) vs. instance/object-level variables  


   3. Differentiate class-level (static) vs. instance/object behaviors/methods 
   

   4. Define class variables (static) as needed '
   
      A. Name 
      B. Data Type 
      C. public / private / final 
      
      
   5. Define instance variables (that you want to be interrelated)  

      A. Name 
      B. Data Type 
      C. private 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Classes-WE1-P1

   Consider writing a class to represent a song on your phone or music player. You  need to define the appropriate attributes (data) to store the name of the song, the artist, and length. All songs should be stored in the same format, which should be MP3.
   
   Complete the following class skeleton.
   
   .. code-block:: java
   
      public class SongType {
         ___A___ ___B___ title;
         ___C___ ___D___ artist;
         ___E___ ___F___ length;
         ___G___ ___H___ final String FORMAT = "MP3";
      }

   .. mchoice:: m-Classes-WE1-P1-1
      :answer_a: public
      :answer_b: private
      :answer_c: String
      :answer_d: int
      :answer_e: double
      :correct: b

      Fill in Blank A.
      
   .. mchoice:: m-Classes-WE1-P1-2
      :answer_a: public
      :answer_b: private
      :answer_c: String
      :answer_d: int
      :answer_e: double
      :correct: c

      Fill in Blank B.
      
   .. mchoice:: m-Classes-WE1-P1-3
      :answer_a: public
      :answer_b: private
      :answer_c: String
      :answer_d: int
      :answer_e: double
      :correct: b

      Fill in Blank C.
      
   .. mchoice:: m-Classes-WE1-P1-4
      :answer_a: public
      :answer_b: private
      :answer_c: String
      :answer_d: int
      :answer_e: double
      :correct: c

      Fill in Blank D.
      
   .. mchoice:: m-Classes-WE1-P1-5
      :answer_a: public
      :answer_b: private
      :answer_c: String
      :answer_d: int
      :answer_e: double
      :correct: b

      Fill in Blank E.
      
   .. mchoice:: m-Classes-WE1-P1-6
      :answer_a: public
      :answer_b: private
      :answer_c: String
      :answer_d: int
      :answer_e: double
      :correct: e

      Fill in Blank F.
      
   .. mchoice:: m-Classes-WE1-P1-7
      :answer_a: public
      :answer_b: private
      :answer_c: static
      :answer_d: void
      :answer_e: const
      :correct: a

      Fill in Blank G.
      
   .. mchoice:: m-Classes-WE1-P1-8
      :answer_a: public
      :answer_b: private
      :answer_c: static
      :answer_d: void
      :answer_e: const
      :correct: c

      Fill in Blank H.
    
.. activecode:: ac-classes-we1-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }