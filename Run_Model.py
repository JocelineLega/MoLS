import MoLS
import matlab

My_test=MoLS.initialize()
My_test.MoLS('./Weather','Test_Data',nargout=0)
My_test.terminate()    
