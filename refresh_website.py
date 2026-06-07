import manifest_generator
import page_generator
import version_generator

if __name__ == "__main__":
    manifest_generator.main()
    page_generator.main()
    version_generator.main()

    print("Website refresh complete!")