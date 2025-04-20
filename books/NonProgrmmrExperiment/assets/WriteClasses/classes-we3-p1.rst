WrClasses-WE3-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 19

    
.. topic:: Subgoals for Writing a Class 3/4

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
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Classes-WE3-P1

   Consider the SongType class you began in an earlier exercise, as illustrated in the following UML diagram.
   
   .. figure:: Figures/song-type-2.PNG
      :alt: UML
   
   Fill in the blanks for the followig code:
   
   .. code-block:: java
   
      public class SongType {
         //attributes declared here
         //...
         
         //getters/accessors
         public ___A___ getTitle () {
            ___B___ ___C___;
         }
         ___D___ String ___E___ () {
            ___F___ artist;
         }
         public ___G___ getLength () {
            ___H___ ___I___;
         }
         
         //setters/mutators
         public ___J___ setTitle (String n) {
            title = ___K___;
         }
         ___L___ void setArtist (___M___ n) {
            artist = ___N___;
         }
         public ___O___ setLength (___P___ n) {
            if (n > 0)
               ___Q___ = n;
         }
      }
   
   
   .. mchoice:: m-Classes-WE3-P1-19
      :answer_a: String
      :answer_b: int
      :answer_c: double
      :answer_d: void
      :answer_e: return
      :correct: a

      Fill in Blank A.
      
   .. mchoice:: m-Classes-WE3-P1-20
      :answer_a: return
      :answer_b: String
      :answer_c: double
      :answer_d: getTitle
      :answer_e: setTitle
      :correct: a

      Fill in Blank B.
      
   .. mchoice:: m-Classes-WE3-P1-21
      :answer_a: return
      :answer_b: String
      :answer_c: title
      :answer_d: getTitle
      :answer_e: setTitle
      :correct: c

      Fill in Blank C.
      
   .. mchoice:: m-Classes-WE3-P1-22
      :answer_a: public
      :answer_b: private
      :answer_c: artist
      :answer_d: getArtist
      :answer_e: setArtist
      :correct: a
      
      Fill in Blank D.
      
   .. mchoice:: m-Classes-WE3-P1-23
      :answer_a: public
      :answer_b: private
      :answer_c: artist
      :answer_d: getArtist
      :answer_e: setArtist
      :correct: d

      Fill in Blank E.
      
   .. mchoice:: m-Classes-WE3-P1-24
      :answer_a: return
      :answer_b: String
      :answer_c: double
      :answer_d: getArtist
      :answer_e: setArtist
      :correct: a

      Fill in Blank F.
      
   .. mchoice:: m-Classes-WE3-P1-25
      :answer_a: String
      :answer_b: int
      :answer_c: double
      :answer_d: void
      :answer_e: return
      :correct: c

      Fill in Blank G.
      
   .. mchoice:: m-Classes-WE3-P1-26
      :answer_a: return
      :answer_b: String
      :answer_c: double
      :answer_d: getLength
      :answer_e: setLength
      :correct: a

      Fill in Blank H.
      
   .. mchoice:: m-Classes-WE3-P1-27
      :answer_a: return
      :answer_b: String
      :answer_c: length
      :answer_d: getLength
      :answer_e: setLength
      :correct: c

      Fill in Blank I.
      
   .. mchoice:: m-Classes-WE3-P1-28
      :answer_a: String
      :answer_b: int
      :answer_c: double
      :answer_d: void
      :answer_e: return
      :correct: d

      Fill in Blank J.
      
   .. mchoice:: m-Classes-WE3-P1-29
      :answer_a: setTitle
      :answer_b: getTitle
      :answer_c: void
      :answer_d: return
      :answer_e: n
      :correct: e

      Fill in Blank K.
      
   .. mchoice:: m-Classes-WE3-P1-30
      :answer_a: public
      :answer_b: private
      :answer_c: artist
      :answer_d: getArtist
      :answer_e: setArtist
      :correct: a
      
      Fill in Blank L.
      
   .. mchoice:: m-Classes-WE3-P1-31
      :answer_a: double
      :answer_b: String
      :answer_c: int
      :answer_d: return
      :answer_e: void
      :correct: b

      Fill in Blank M.
      
   .. mchoice:: m-Classes-WE3-P1-32
      :answer_a: setArtist
      :answer_b: getArtist
      :answer_c: void
      :answer_d: return
      :answer_e: n
      :correct: e

      Fill in Blank N.
      
   .. mchoice:: m-Classes-WE3-P1-33
      :answer_a: String
      :answer_b: int
      :answer_c: double
      :answer_d: void
      :answer_e: return
      :correct: d

      Fill in Blank O.
      
   .. mchoice:: m-Classes-WE3-P1-34
      :answer_a: double
      :answer_b: String
      :answer_c: int
      :answer_d: return
      :answer_e: void
      :correct: a

      Fill in Blank P.
      
   .. mchoice:: m-Classes-WE3-P1-35
      :answer_a: return
      :answer_b: length
      :answer_c: double
      :answer_d: getLength
      :answer_e: setLength
      :correct: b

      Fill in Blank Q.
      
    
   
.. activecode:: ac-classes-we3-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }