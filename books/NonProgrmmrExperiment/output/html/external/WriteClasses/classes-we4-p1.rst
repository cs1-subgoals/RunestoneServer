WrClasses-WE4-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 36

    
.. topic:: Subgoals for Writing a Class 4/4

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
      
      
   6. Create constructor (behavior) that creates initial state of object  

      A. public
      B. Same name as class
      C. No return type
      D. Default - no parameters
      E. Logic - initialize all variables
      F. Repeat as needed, adding parameters 
      
   
   7.  Create 1 accessor and 1 mutator behaviors per attribute

      A. Accessors 

         a. Name is get_<attr_name> 
         b. Public 
         c. Return type same data type as attribute
         d. No parameters 
         e. Logic - return value

      B. Mutators 
      
         a. Name is set_<attr_name>
         b. Public
         c. Return type is void 
         d. Parameter is same data type as attribute
         e. Logic validates input parameter and sets attribute value 
         
      
   8. Write toString method
   
      A. public
      B. Returns String
      C. No parameters
      D. Logic - convert needed attributes to a format that can be printed 
   
   9. Write equals method 
   
      A. public 
      B. Returns boolean
      C. Parameter - instance of the class
      D. Logic - compare attributes for equity
      
   10. Create additional methods as needed 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Classes-WE4-P1

   Consider the SongType class you began in an earlier exercise, as illustrated in the following UML diagram.
   
   .. figure:: Figures/song-type-3.PNG
      :alt: UML
   
   For questions 36 - 39, fill in the code blanks to implement the toString method to print the song in the following format: ``SONG by ARTIST (X.XX)`` where X.XX is the length in minutes.
   
   .. code-block:: java
   
      public ___A___ toString () {
         return ___B___ + " by " + ___C___ + "(" + ___D___ + ")";
      
   
   .. mchoice:: m-Classes-WE4-P1-36
      :answer_a: String
      :answer_b: int
      :answer_c: double
      :answer_d: void
      :answer_e: return
      :correct: a

      Fill in Blank A.
      
   .. mchoice:: m-Classes-WE4-P1-37
      :answer_a: void
      :answer_b: String
      :answer_c: title
      :answer_d: artist
      :answer_e: length
      :correct: c

      Fill in Blank B.
      
   .. mchoice:: m-Classes-WE4-P1-38
      :answer_a: void
      :answer_b: String
      :answer_c: title
      :answer_d: artist
      :answer_e: length
      :correct: d

      Fill in Blank C.
      
   .. mchoice:: m-Classes-WE4-P1-39
      :answer_a: void
      :answer_b: String
      :answer_c: title
      :answer_d: artist
      :answer_e: length
      :correct: e
      
      Fill in Blank D.
      
   For questions 40 - 45, fill in the code blanks to implement the equals method, where two songs are equal if
   
   .. code-block:: java
   
      public ___E___ equals (___F___ other) {
         return artist.___G___(other.___H___) &&
            title.___I___(other.___J___);
      }
      
   .. mchoice:: m-Classes-WE4-P1-40
      :answer_a: void
      :answer_b: String
      :answer_c: boolean
      :answer_d: SongType
      :answer_e: other
      :correct: c

      Fill in Blank E.
      
   .. mchoice:: m-Classes-WE4-P1-41
      :answer_a: void
      :answer_b: String
      :answer_c: boolean
      :answer_d: SongType
      :answer_e: other
      :correct: d

      Fill in Blank F.
      
   .. mchoice:: m-Classes-WE4-P1-42
      :answer_a: artist
      :answer_b: title
      :answer_c: length
      :answer_d: other
      :answer_e: equals
      :correct: e

      Fill in Blank G.
      
   .. mchoice:: m-Classes-WE4-P1-43
      :answer_a: artist
      :answer_b: title
      :answer_c: length
      :answer_d: other
      :answer_e: equals
      :correct: a

      Fill in Blank H.
      
   .. mchoice:: m-Classes-WE4-P1-44
      :answer_a: artist
      :answer_b: title
      :answer_c: length
      :answer_d: other
      :answer_e: equals
      :correct: e

      Fill in Blank I.
      
   .. mchoice:: m-Classes-WE4-P1-45
      :answer_a: artist
      :answer_b: title
      :answer_c: length
      :answer_d: other
      :answer_e: equals
      :correct: d

      Fill in Blank J.
      
   For questions 46 - 50, fill in the code blanks to implement a method called isLonger, which returns true if the song is longer than the song in the parameter.
   
   .. code-block:: java
   
      public ___K___ isLonger (___L___ other) {
         return ___M___ > ___N___.___O___;
      }
      
   .. mchoice:: m-Classes-WE4-P1-46
      :answer_a: void
      :answer_b: String
      :answer_c: boolean
      :answer_d: SongType
      :answer_e: other
      :correct: c

      Fill in Blank K.
      
   .. mchoice:: m-Classes-WE4-P1-47
      :answer_a: void
      :answer_b: String
      :answer_c: boolean
      :answer_d: SongType
      :answer_e: other
      :correct: d
      
      Fill in Blank L.
      
   .. mchoice:: m-Classes-WE4-P1-48
      :answer_a: artist
      :answer_b: title
      :answer_c: length
      :answer_d: other
      :answer_e: equals
      :correct: c

      Fill in Blank M.
      
   .. mchoice:: m-Classes-WE4-P1-49
      :answer_a: artist
      :answer_b: title
      :answer_c: length
      :answer_d: other
      :answer_e: equals
      :correct: d

      Fill in Blank N.
      
   .. mchoice:: m-Classes-WE4-P1-50
      :answer_a: artist
      :answer_b: title
      :answer_c: length
      :answer_d: other
      :answer_e: equals
      :correct: c

      Fill in Blank O.
      
   
   
.. activecode:: ac-classes-we4-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }