# 文件名解析、遍历统计、JSON 导出
import json
from pathlib import Path
# 文件名解析
def read_file(audio_dir):
    audio_dir = Path(audio_dir)
    if not audio_dir.exists() or not audio_dir.is_dir():
        print(f'{audio_dir}不存在或不是目录路径')
        return []
    wav_file = list(audio_dir.glob('*.wav'))
    if not wav_file:
        print('不存在wav文件')
    return wav_file
# 遍历统计-->说话人ID_样本编号_标签.wav-->说话人数量、真假样本数
def audio_statistics(wav_file:list):
    stats = {
        'total_file':0,
        'speaker_count':0,
        'real_total_count':0,
        'fake_total_count':0,
        'detail':{}
    }
    for file in wav_file:
        file = Path(file)
        parts = file.stem.split('_')
        if len(parts) < 3 or parts[-1] not in ('real','fake'):
            print(f'跳过格式异常文件：{file.name}')
            continue
        speaker_id = parts[0]
        label = parts[-1]
        stats['total_files'] += 1
        if speaker_id not in stats['detail']:
            stats['detail'][speaker_id] = {
                "real_count": 0,
                "fake_count": 0,
            }
        detail = stats['detail'][speaker_id]
        if label == 'real':
            stats['real_total_count'] += 1
            detail['real_count'] += 1
        elif label == 'fake':
            stats['fake_total_count'] += 1
            detail['fake_count'] += 1
    stats['speaker_count'] = len(stats['detail'])
    return stats
def export_json(output_dir,stats):
    output_path = Path(output_dir)
    # 创建目录
    output_path.mkdir(parents=True,exist_ok=True)
    output_file = output_path/'output.json'
    with open(output_file,'w',encoding='utf-8') as f:
        json.dump(stats,f,ensure_ascii=False,indent=2,sort_keys=True)
        print(f'统计结果已导出到：{output_file.resolve()}')