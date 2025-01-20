import subprocess

class balloon_hash:
    def generate(password: str, space_cost: int, time_cost: int, parallel_cost: int = 1) -> str:
        # 定義執行檔路徑和參數
        executable = "./build/balloon/balloon"
        
        # 用單引號保護或使用轉義
        command = [executable, password, "-t", str(time_cost), "-s", str(space_cost), "-p", str(parallel_cost)]

        # 執行命令
        result = subprocess.run(command, text=True, capture_output=True)
        
        assert result.returncode == 0, result.stderr
        
        return result.stdout
    
    def verify(password: str, hash_blob: str) -> bool:
        # 定義執行檔路徑和參數
        executable = "./build/balloon/balloon"
        # 用單引號保護或使用轉義
        command = [executable, password, f"--blob={hash_blob}"]

        # 執行命令
        result = subprocess.run(command, text=True, capture_output=True)
        return result.returncode == 0
    
test_blob = balloon_hash.generate("123", 12288, 3)
print("gen: ",test_blob)
# test_blob2 = balloon_hash.verify("123", test_blob)
# print("ver: ",test_blob2)
