from argparse import ArgumentParser
import os
import shutil

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--dataset_dir', type=str, default='./input_data')
    parser.add_argument('--output_dir', type=str, default='./cd_dataset')

    args = parser.parse_args()
    
    # Create output directory if not exists
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        print(f"Direcotry created: {args.output_dir}")
    
    # Create subdirectories
    if not os.path.exists(os.path.join(args.output_dir, 'A')):
        os.makedirs(os.path.join(args.output_dir, 'A'))
        print(f"Direcotry A created: {os.path.join(args.output_dir, 'A')}")
    if not os.path.exists(os.path.join(args.output_dir, 'B')):
        os.makedirs(os.path.join(args.output_dir, 'B'))
        print(f"Direcotry B created: {os.path.join(args.output_dir, 'B')}")
    if not os.path.exists(os.path.join(args.output_dir, 'label')):
        os.makedirs(os.path.join(args.output_dir, 'label'))
        print(f"Direcotry label created: {os.path.join(args.output_dir, 'label')}")
    if not os.path.exists(os.path.join(args.output_dir, 'list')):
        os.makedirs(os.path.join(args.output_dir, 'list'))
        print(f"Direcotry list created: {os.path.join(args.output_dir, 'list')}")
        
    output_list_dir = os.path.join(args.output_dir, 'list')
    
    # Copy files from train, test and val to subdirectories
    for folder in ['train', 'test', 'val']:
        with open(os.path.join(output_list_dir, folder+'.txt'), 'a') as f:
            for subfolder in ['A', 'B', 'label']:
                src = os.path.join(args.dataset_dir, folder, subfolder)
                dst = os.path.join(args.output_dir, subfolder)
                for file in os.listdir(src):
                    shutil.copyfile(os.path.join(src, file), os.path.join(dst, file))
                    print(f"File copied: {os.path.join(src, file)} -> {os.path.join(dst, file)}")
                    f.write(file + '\n')

    
    